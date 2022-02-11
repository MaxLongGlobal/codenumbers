import os
import prettytable as pt

'''
py ./code/calculatelines.py ../codenumbers/code
'''

TXT_SUFFIX_SET = {'.txt'}
C_SUFFIX_SET = {'.c'}
PYTHON_SUFFIX_SET = {'.py'}
JAVA_SUFFIX_SET = {'.java'}
HTML_SUFFIX_SET = {'.html'}
CSS_SUFFIX_SET = {'.css'}
JSON_SUFFIX_SET = {'.json'}
XML_SUFFIX_SET = {'.xml'}
CPP_SUFFIX_SET = {'.h', '.hpp', '.hxx', '.c', '.cpp', '.cc', '.cxx'}

#
txt_lines = 0
c_lines = 0
python_lines = 0
java_lines = 0
cpp_lines = 0
html_lines = 0
css_lines = 0
json_lines = 0
xml_lines = 0
total_lines = 0


def list_files(path, tag):
    '''

    '''
    if tag == 1:
        count_lines(path)
    else:
        filenames = os.listdir(path)
        # if filenames.find('venv') == -1:
        print(filenames)
        for f in filenames:
            fpath = os.path.join(path, f)
            if (os.path.isfile(fpath)):
                count_lines(fpath)
            if (os.path.isdir(fpath)) and fpath.find('venv') == -1:
                list_files(fpath, tag)


def count_lines(fpath):
    '''
    '''
    global CPP_SUFFIX_SET, C_SUFFIX_SET, TXT_SUFFIX_SET,PYTHON_SUFFIX_SET, JAVA_SUFFIX_SET
    global cpp_lines, c_lines, txt_lines, python_lines, java_lines, html_lines, css_lines, json_lines, xml_lines, total_lines


    with open(fpath, 'rb') as f:
        cnt = 0
        last_data = '\n'
        while True:
            data = f.read(0x400000)
            if not data:
                break
            cnt += data.count(b'\n')
            last_data = data
        if last_data[-1:] != b'\n':
            cnt += 1

    suffix = os.path.splitext(fpath)[-1]

    if suffix in C_SUFFIX_SET:
        c_lines += cnt
    elif suffix in TXT_SUFFIX_SET:
        txt_lines += cnt
    elif suffix in PYTHON_SUFFIX_SET:
        python_lines += cnt
    elif suffix in JAVA_SUFFIX_SET:
        java_lines += cnt
    elif suffix in HTML_SUFFIX_SET:
        html_lines += cnt
    elif suffix in CSS_SUFFIX_SET:
        css_lines += cnt
    elif suffix in JSON_SUFFIX_SET:
        json_lines += cnt
    elif suffix in XML_SUFFIX_SET:
        xml_lines += cnt
    elif suffix in CPP_SUFFIX_SET:
        cpp_lines += cnt
    else:
        pass


def print_result():
    '''

    '''
    global tb, tg
    global cpp_lines, python_lines, java_lines, total_lines, c_lines, txt_lines, html_lines, css_lines, json_lines, xml_lines

    tb = pt.PrettyTable()
    tb.field_names = ['C', 'TXT', 'PYTHON', 'JAVA', 'HTML', 'CSS', 'JSON', 'XML', 'Others', 'TOTAL']
    tb.add_row([c_lines, txt_lines, python_lines, java_lines, html_lines, css_lines, json_lines, xml_lines, cpp_lines, total_lines])
    tg = tb
    # print(tb)
    #
    tb = None
    c_lines, txt_lines, python_lines, java_lines, html_lines, css_lines, json_lines, xml_lines, cpp_lines, total_lines = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    return tg


def get_all_code_numbers(path, tgg):
    global total_lines
    # if (len(sys.argv) != 2):
    #     print("Usage : python3 code_analyst.py project_path")
    # else:
    #     project_path = sys.argv[1]
    #     list_files(project_path)
    #
    #     total_lines = cpp_lines + python_lines + java_lines
    #     print_result()

    project_path = path
    list_files(project_path, tgg)

    total_lines = cpp_lines + c_lines + txt_lines + python_lines + java_lines + html_lines + css_lines + json_lines + xml_lines

    return print_result()
