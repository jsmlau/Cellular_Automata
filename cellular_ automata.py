"""
Cellular Automata

Created by Jas Lau on 7/9/19.
Copyright © 2019 Jas Lau. All rights reserved.

"""
import math
import numpy


# ====================== Automaton Class ======================

class Automaton:
    # various class constants -----------------------
    RULES_SIZE_32BITS = 32
    RULES_SIZE = 8
    BITS_IN_RULE_SIZE = int(math.log(RULES_SIZE, 2))  # 3
    BITS_IN_RULE_SIZE_32 = int(math.log(RULES_SIZE_32BITS, 2))  # 5
    MIN_DISPLAY_WIDTH = 20
    MAX_DISPLAY_WIDTH = 121
    DFLT_DISPLAY_WIDTH = 99
    MIN_RULE = 0
    MAX_RULE = 2 ** RULES_SIZE - 1  # 255 for us
    MAX_RULE_32BITS = 2 ** RULES_SIZE_32BITS - 1
    DFLT_RULE = 126
    ON_STR = "*"
    OFF_STR = " "

    # constructor for 8 bits-------------------------------------
    def __init__(self, rule=DFLT_RULE, bits=BITS_IN_RULE_SIZE):
        if bits == self.RULES_SIZE:
            # Set rule[] to all "0" (false)
            self.rule = numpy.zeros(self.RULES_SIZE, dtype=bool)
            if not self.set_rule(rule):
                self.set_rule(self.DFLT_RULE)

        elif bits == self.RULES_SIZE_32BITS:
            self.rule = numpy.zeros(self.RULES_SIZE_32BITS, dtype=bool)
            if not self.set_rule_32bits(rule):
                self.set_rule_32bits(self.DFLT_RULE)

        self.extreme_bit = self.OFF_STR
        self.display_width = self.MAX_DISPLAY_WIDTH
        self.this_gen = self.ON_STR
        self.reset_first_gen()
        self.set_display_width(self.DFLT_DISPLAY_WIDTH)

    # mutators for 8 bits----------------------------------------
    def set_rule(self, rule):
        """Convert the integer (rule) to 8-bit binary number.

        Args:
            rule (int): The rule's number

        Returns:
            bool: True for current bit is 1. False otherwise.
        """
        if not (type(rule) == int) and (self.MIN_RULE <= rule <= self.MAX_RULE):
            return False
        # Convert from integer to 8-bits bools
        for i in range(self.RULES_SIZE):
            bit = 1 << i & rule
            if bit == 0:
                self.rule[i] = False
            else:
                self.rule[i] = True
        return True

    # mutators for 32 bits----------------------------------------
    def set_rule_32bits(self, rule):
        """Similar to set_rule(rule) but the bool type rule [] stores 32-bit binary number.

        Args:
            rule (int): The rule's number

        Returns:
            bool: True for current bit is 1. False otherwise.
        """
        if not (type(rule) == int) and (self.MIN_RULE <= rule <=
                                        self.MAX_RULE_32BITS):
            return False
        # Convert from integer to 32-bits bools
        for i in range(self.RULES_SIZE_32BITS):
            bit = 1 << i & rule
            if bit == 0:
                self.rule[i] = False
            else:
                self.rule[i] = True
        return True

    def reset_first_gen(self):
        """Create a virtual 1 in a sea of 0s"""        
        self.this_gen = "*"
        self.extreme_bit = " "

    def propagate_new_generation(self):
        """Generate next line based on rule and current this_gen."""        
        blank = self.extreme_bit * (self.BITS_IN_RULE_SIZE - 1)
        self.this_gen = blank + self.this_gen + blank

        next_gen = ""
        # start from index 1 element (the middle element of triplet)
        for i in range(1, len(self.this_gen) - 1):
            triplet = 0
            power = 2 * 2
            # since the sliding window is three, we also need to get the element from index 0 to index 2
            for j in range(-1, 2):
                # looping each element in triplet
                if self.this_gen[i + j] == self.ON_STR:
                    triplet += power
                power /= 2

            # generate new gen based on rule
            # print("triplet", triplet) #debug
            if self.rule[int(triplet)]:
                next_gen += self.ON_STR
            else:
                next_gen += self.OFF_STR

        if self.extreme_bit == self.OFF_STR:
            extreme_bit_rule = self.rule[0]
        else:
            extreme_bit_rule = self.rule[self.RULES_SIZE - 1]

        # convert to "*" or " "
        if extreme_bit_rule:
            self.extreme_bit = self.ON_STR
        else:
            self.extreme_bit = self.OFF_STR

        self.this_gen = next_gen

    def propagate_new_generation_32bits(self):
        """32-bit version of propagate_new_generation."""
        # pad 6 blank at front and end.
        blank = self.extreme_bit * (self.BITS_IN_RULE_SIZE_32 - 1)
        self.this_gen = blank + self.this_gen + blank
        # print("len",len(self.this_gen), "blank ", len(blank)) #debug
        next_gen = ""

        # start from index 2 element (the middle element of quintuplet)
        for i in range(2, len(self.this_gen) - 2):
            quintuplet = 0
            # binary power is 5 for 32-bits
            power = 2 ** 4
            # since the sliding window is quintuplet, we also need to get the
            # element from index 0 and index 4
            for j in range(-2, 3):
                # looping each element in quintuplet
                if self.this_gen[i + j] == self.ON_STR:
                    quintuplet += power
                power /= 2

            # generate new gen based on rule
            if self.rule[int(quintuplet)]:
                next_gen += self.ON_STR
            else:
                next_gen += self.OFF_STR

        if self.extreme_bit == self.OFF_STR:
            extreme_bit_rule = self.rule[0]
        else:
            extreme_bit_rule = self.rule[self.RULES_SIZE_32BITS - 1]

        # convert to "*" or " "
        if extreme_bit_rule:
            self.extreme_bit = self.ON_STR
        else:
            self.extreme_bit = self.OFF_STR

        self.this_gen = next_gen

    def to_string_current_gen(self):
        """Print function"""
        pad_len = (self.display_width - len(self.this_gen)) // 2
        pad = ""

        if pad_len >= 0:
            for i in range(0, pad_len):
                pad += self.extreme_bit
            ret_str = pad + self.this_gen + pad
        else:
            ret_str = self.this_gen[-pad_len:-pad_len + self.display_width]
        return ret_str

    def set_display_width(self, width=DFLT_DISPLAY_WIDTH):
        """Set the display width.

        Args:
            width : width to display. Defaults to DFLT_DISPLAY_WIDTH.

        Returns:
            bool: True for successfully set the display width. False otherwise.
        """        
        if not ((type(width) == int) and width % 2 == 1 and (
                self.MIN_DISPLAY_WIDTH <= width <= self.MAX_DISPLAY_WIDTH)):
            return False

        self.display_width = width
        return True


# ====================== End Class Automaton ======================

# ======================== Client (As a Function) =======================
def main():
    user_input_bit = int(input("\nWhich bits rule are you choosing (8-bit or "
                               "32-bit)? "))
    if user_input_bit is 8:
        # get rule from user
        valid_rule_given = False
        while not valid_rule_given:
            try:
                rule = int(input("Enter Rule ({} - {}): ".format(
                    Automaton.MIN_RULE,
                    Automaton.MAX_RULE)))
                if not (Automaton.MIN_RULE <= rule <= Automaton.MAX_RULE):
                    print(" ** please enter an integer in the specified range **")
                else:
                    valid_rule_given = True
            except (TypeError, ValueError) as err:
                print("  ** {} \n   please enter an integer in the "
                      "specified range.\n".format(err))
        #  create automaton with this rule and single central dot
        aut = Automaton(rule, user_input_bit)
        # now show it
        print("   start")
        for k in range(50):
            print(aut.to_string_current_gen())
            aut.propagate_new_generation()
        print("   end")

    elif user_input_bit is 32:
        # get rule from user
        valid_rule_given_32bits = False
        while not valid_rule_given_32bits:
            try:
                rule = int(input("Enter Rule for 32 Bits({} - {}): ".format(
                    Automaton.MIN_RULE, Automaton.MAX_RULE_32BITS)))
                if not (Automaton.MIN_RULE <= rule <= Automaton.MAX_RULE_32BITS):
                    print(" ** please enter an integer in the specified range **")
                else:
                    valid_rule_given_32bits = True
            except (TypeError, ValueError) as err:
                print("  ** {} \n   please enter an integer in the specified "
                      "range.\n".format(err))

        #  create automaton with this rule and single central dot
        aut = Automaton(rule, user_input_bit)

        # now show it
        print("   start")
        for k in range(50):
            print(aut.to_string_current_gen())
            aut.propagate_new_generation_32bits()
        print("   end")


# ======================= End of Client (As a Function) ======================

if __name__ == "__main__":
    main()

