class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        for name in path.split("/"):
            if name == "..":
                if len(directories)>0:
                    directories.pop()
            elif name != "" and name != ".":
                directories.append(name)
                
        simplePath = "/" + "/".join(directories)
        
        return simplePath
                    