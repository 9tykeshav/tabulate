class Tabu :

    def __init__(self , headers ) :

        self.headers = headers

        self.tabulated = ""

        self.w = 0

        self.am = []

    def add (self , data ) :

        w = [len(i) + 2 for i in data if self.w <= len(i)  ]

        for width in w :

            if self.w <  width :

                self.w = width

       # print(self.w)

        self.am.append(data)

       # print(self.am)

    def render(self) :

        for header in self.headers :

            self.tabulated +=  "|" + header + (self.w - len(header)  ) * " "

        self.tabulated += f"""\n{self.w * len(self.headers) * "_"}\n"""

        for rows in self.am :

            for fields in rows :

                self.tabulated += f"|{fields}" + (self.w - len(fields) ) * " "

            self.tabulated += "\n"

        print("_" * (len(self.headers) * self.w) )

        print(self.tabulated)

a = Tabu(["something" , "not somethin" , "epic" ])

for i in range(5) :

    a.add(["ok" , "lmk" , "owl"])

a.add(["djsjsjsj" ," 7       37373" , "&£&£&£" ])

a.add(["iejdj" , "rheh" , "rueu" ])

a.render()
