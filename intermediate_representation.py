class SourceFile(object):

    def __init__(self):
        self.translation_unit_list = []

    def append(self, translation_unit):
        self.translation_unit_list.append(translation_unit)

    # TODO: Uncomment once every translation unit will be handled
    # def __repr__(self):
    #     s = '\n'.join(self.translation_unit_list)
    #     return s

class Struct(object):
    """
    """

    def __init__(self, identifier, declaration_list = [], packing = 4):
        self.identifier       = identifier
        self.declaration_list = declaration_list
        self.packing          = packing

    def is_incomplete(self):
        return not len(self.declaration_list_list)

    def __repr__(self):
        s = f'''
                Struct name: {self.identifier} 
                Declaration list: {self.declaration_list} 
                Packing: {self.packing} 
            '''
        return s

class Union(object):
    """
    """

    def __init__(self, identifier, declaration_list = [], packing = 4):
        self.identifier       = identifier
        self.declaration_list = declaration_list
        self.packing          = packing

    def is_incomplete(self):
        return not len(self.declaration_list)

    def __repr__(self):
        s = f'''
                Union name: {self.union_name} 
                Declaration list: {self.declaration_list} 
                Packing: {self.packing} 
            '''
        return s

class StructDeclaration(object):
    """
    """

    def __init__(self, specifier_qualifier_list, struct_declarator_list):
        self.specifier_qualifier_list = specifier_qualifier_list
        self.struct_declarator_list   = struct_declarator_list

    def __repr__(self):
        new_line = '\n' 
        s = f'''
                {" ".join(self.specifier_qualifier_list)} {self.struct_declarator_list[:]};
            '''
        return s

class StructDeclarator(object):
    """
    """
    def __init__(self, declarator = '', bitfield = None):
        self.declarator = declarator
        self.bitfield = bitfield

    def __repr__(self):
        return f'''{self.declarator}{f':{self.bitfield}' if self.bitfield else ''}'''

class Enumeration(object):

    def __init__(self, identifier = None, enumerator_list = [], packing = 4):
        self.identifier      = identifier
        self.enumerator_list = enumerator_list
        self.packing         = packing

    def is_incomplete(self):
        return not len(self.enumerator_list)

    def __repr__(self):
        s = f'''
                Enumeration name: {self.identifier}
                Enumerator list: {self.enumerator_list}
                Packing : {self.packing}'''
        return s

class Function(object):
    
    def __init__(self):
        pass

class Macro(object):

    def __init__(self, name, replacement = '', arg_list = [], variadic = False, callback = None):
        self.name              = name
        self.replacement       = replacement
        self.arg_list          = arg_list
        self.variadic          = variadic
        self.callback          = callback
        self.has_been_expanded = False

    def expand(self, arg_list = []):
        """
        Expand a macro. 

        :param      arg_list:  The argument list
        :type       arg_list:  { type_description }
        """
        replacement = self.replacement

        if arg_list:
            if not self.variadic and len(arg_list) != len(self.arg_list):
                raise Exception("Number of arguments not matching with expected list length.")

            if self.callback:
                raise Exception("Callback macro can't be called with user provided argument list.")

            for label, arg in zip(self.arg_list, arg_list): 
                replacement = replacement.replace(label, arg)

        elif self.callback:
            callback_return = self.callback(*self.arg_list)
            if type(callback_return) == str:
                replacement = f'"{callback_return}"'
            else:
                replacement = str(callback_return)
        elif self.arg_list and not arg_list:
            raise Exception("Function like macro needs argument list.")

        self.has_been_expanded = True

        return replacement

    def __repr__(self):
        s = f'''
                Macro name: {self.name}
                Replacement text: {self.replacement}
                Argument list : {self.arg_list}
                Variadic : {self.variadic}'''
        return s