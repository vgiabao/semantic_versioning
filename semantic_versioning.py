#!/usr/bin/env python3


def check_integer_error(s):
    '''
    check each fragment of input if it can transfer to integer
    :param s: string input
    :return: boolean depends on the length of string and the type
    of each partition of input
    '''
    for item in s:
        try:
            int(item)
        except (TypeError, ValueError):
            return True
    if len(s) > 3:
        return True
    return False


def check_tuple(s):
    '''
    checking s if is tuple
    '''
    return isinstance(s, tuple)


def add_zero(s):
    '''
    add zero numbers
    :param s: list
    :return: tuple comprises 3 number
    '''
    if len(s) == 1:
        s.append(0)
        s.append(0)
        return tuple(s)
    elif len(s) == 2:
        s.append(0)
        return tuple(s)
    return tuple(s)


def compare_two_tuple(this, other):
    '''

    compare each part of 2 tuple
    :param this: version 1
    :param other: version 2
    :return: -1 if this version is older, 1 if this version is newer,
    0 if they are similar

    '''
    return -1 if this < other else 0 if this == other else 1


def compare_version(this, other):
    '''
    check type of this and other and compare them
    :param this: version 1
    :param other: version 2
    :return: compared result
    '''
    if check_integer_error(this) or check_integer_error(other):
        return 'Type error, inputs should be number'
    if check_tuple(this) and check_tuple(other):
        return compare_two_tuple(this, other)
    return 'Type Error, we need two tuples'


def convert_string_to_version_component_numbers(s):
    s = s.split('.')
    if not check_integer_error(s):
        return add_zero(s)
    return 'Type error, inputs should be number'


class Version:
    def __init__(self, major=None, minor=None, patch=None):
        if check_tuple(major):
            self.major, self.minor, self.patch = add_zero(list(major))
        elif isinstance(major, str) and minor is None:
            self.major, self.minor, self.patch = \
                convert_string_to_version_component_numbers(major)
        else:
            self.major = major
            self.minor = minor
            self.patch = patch
        self.information = (int(self.major), int(self.minor), int(self.patch))

    def __repr__(self):
        return ('Version({}, {}, {}'.format(self.major, self.minor,
                                            self.patch))

    def __str__(self):
        if not check_integer_error((self.major, self.minor, self.patch)):
            return '{}.{}.{}'.format(self.major, self.minor, self.patch)
        return 'input must be integer'

    def __gt__(self, other):
        return compare_two_tuple(self.information, other.information) == 1

    def __lt__(self, other):
        return compare_two_tuple(self.information, other.information) == -1

    def __eq__(self, other):
        return compare_two_tuple(self.information, other.information) == 0


if __name__ == '__main__':
    # s1 = (0,0,0)
    # s2 = (0,0,1)
    # print(convert_string_to_version_component_numbers(s))
    version1 = Version('00.0.000')
    version2 = Version('0.0.0')
    print(version1 == version2)
