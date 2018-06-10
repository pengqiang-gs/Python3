# _*_ coding: utf-8 _*_

from tkinter import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widget()

    def create_widget(self):
        self._input = Entry(self)
        self._input.pack()
        self._greet = Button(self, text = '打招呼', command = self.greeting)
        self._greet.pack()

    def greeting(self):
        name = self._input.get() or '陌生人'
        messagebox.showinfo('提醒消息', '您好， %s' % name)

if __name__ == '__main__':
    app = Application()
    app.master.title('专注于打招呼')
    app.mainloop()
