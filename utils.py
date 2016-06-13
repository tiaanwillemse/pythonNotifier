
def object_to_string (object):
    string = ''
    for prop, value in object.iteritems():
        if string == '':
            string += '{'
        else:
            string += ', '
         
        string += '"' + prop+ '" : ';
        if(isinstance(value, (str, basestring))):
            string += '"' + value + '"'
        elif (isinstance(value, (tuple, list, dict, set))):
            string += self.object_to_string(value)
        else:
            string += 'ERROR'
        
    string += '}'

    return string;
