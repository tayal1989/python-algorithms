import re

################Simple Example########################
print(re.split(r'\s*', 'Here  * are some words'))   # \s is signifying space character, even we are using multiple spaces after Here, it is considering as
                                                   # a single space
                                                # * - 0 or more - any no of characters
                                                # O/P - ['Here', '*', 'are', 'some', 'words']

print(re.split(r'(\s*)', 'Here are some words'))   # () - used for grouping or including, actually including space in the output list
                                                  # O/P - ['Here', ' ', 'are', ' ', 'some', ' ', 'words']

print(re.split(r'(s*)', 'Here are some words'))   # / is missing - means string will split on basis of word 's'
                                                 # ['Here are ', 's', 'ome word', 's', '']

#######################################################

print(re.split(r'[a-f]', 'djhfahfvs?"HA;FcR.'))      # splits on basis of any character which is coming in between letters a and f
                                                    # [] - means to include range of character
                                                    # O/P - ['', 'jh', '', 'h', 'vs?"HA;F', 'R.']

print(re.split(r'[a-fA-F]', 'djhfahfvs?HA;FcR.', re.I | re.M))      # re.I - FLAGS - means ignore case
                                                                 # re.M - FLAGS - means multiline i.e. for multiple input lines instead of 1 line
                                                                 # O/P - ['', 'jh', '', 'h', 'vs?H', ';', '', 'R.']

print(re.split(r'[a-fA-F0-9]', 'djhfahfvs?HA;FcR.', re.I | re.M))      # re.I - FLAGS - means ignore case
                                                                 # re.M - FLAGS - means multiline i.e. for multiple input lines instead of 1 line
                                                                 # O/P - ['', 'jh', '', 'h', 'vs?H', ';', '', 'R.']

print(re.split(r'[a-f][a-f]', 'djhfahfvs?HA;FcR.', re.I | re.M))      # [][] - for multiple characters
                                                                     # O/P - ['djh', 'hfvs?HA;FcR.']

#########################################################
#In this example, we have to find specially "324 main st."
                                                                     
print(re.findall(r'\d', "finqwen324 main st.iewasd", re.I|re.M))         # \d - digits, \D - non-digits, \S - non-space
                                                                        # \d is similar to [0-9]
                                                                        # O/P - ['3', '2', '4']

print(re.findall(r'\d*', "finqwen324 main st.iewasd", re.I|re.M))        # * - 0 or more
                                                                        # + - 1 or more
                                                                        # ? - 0 or 1 of
                                                                        # {5} - exact number of
                                                                        # {1, 60} - range on number of
                                                                        # O/P - ['', '', '', '', '', '', '', '324', '', '', '', '', '',
                                                                        # '', '', '', '', '', '', '', '', '', '', '']

print(re.findall(r'\d+', "finqwen324 main st.iewasd", re.I|re.M))        # * - 0 or more
                                                                        # + - 1 or more
                                                                        # ? - 0 or 1 of
                                                                        # {5} - exact number of characters
                                                                        # {1, 60} - range on number of
                                                                        # O/P - ['324']

print(re.findall(r'\d?', "finqwen324 main st.iewasd", re.I|re.M))        # * - 0 or more
                                                                        # + - 1 or more
                                                                        # ? - 0 or 1 of
                                                                        # {5} - exact number of characters
                                                                        # {1,60} - range on number of
                                                                        # O/P - ['', '', '', '', '', '', '', '3', '2', '4', '', '', '',
                                                                        # '', '', '', '', '', '', '', '', '', '', '', '', '']

print(re.findall(r'\d{1,5}', "finqwen324123 main st.iewasd", re.I|re.M))    # * - 0 or more
                                                                        # + - 1 or more
                                                                        # ? - 0 or 1 of
                                                                        # {5} - exact number of characters
                                                                        # {1,5} - exact number of digits - min - 1 - max - 5
                                                                        # O/P - ['32412', '3']

print(re.findall(r'\d{1,5}\s\w+', "finqwen324 main st.iewasd", re.I|re.M))    # \w - alphanumeric     + = 1 or main characters
                                                                            # O/P - ['324 main']

print(re.findall(r'\d{1,5}\s\w+\s\w+\.', "finqwen324 main st.iewasd", re.I|re.M))    # \. - regular period (.)
                                                                                    # . - Any character but newline(\n)
                                                                                    # O/P - ['324 main st.']
                                                                                    # .* - look for anything that comes between


