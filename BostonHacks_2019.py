#
#
#
# located on Desktop

import aesthetics_courses.txt
import math

def clean_text(txt):
    course_code = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text_length = len(txt)
    st += ''
    for course in range(text_length):
        if txt[course] not in course_code:
            st += ''
        else:
            st += txt[course]
    return st

    
    
