class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        # Split the path by '/' and iterate over each component
        for component in path.split('/'):
            if component == '..':
                if stack:
                    stack.pop()  # Go up one directory level
            elif component and component != '.':
                stack.append(component)  # Add valid directory name to the stack
        # Construct the simplified path
        return '/' + '/'.join(stack)
