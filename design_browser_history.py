class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.current = homepage
        self.b = []
        self.f = []

    def visit(self, url: str) -> None:
        self.b.append(self.current)
        self.f = []
        self.current = url

    def back(self, steps: int) -> str:
        while self.b and steps>0:
            steps -= 1
            self.f.append(self.current)
            self.current = self.b.pop()
        return self.current
            
    def forward(self, steps: int) -> str:
        while self.f and steps>0:
            steps -= 1
            self.b.append(self.current)
            self.current = self.f.pop()
        return self.current
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)