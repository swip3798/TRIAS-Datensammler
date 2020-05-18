class LineFilter():
    def __init__(self, line, direction = None):
        '''
        Filter for specifying a line
        line: string
        *direction: LineDirection (enum)
        '''
        self.line = line
        self.direction = direction