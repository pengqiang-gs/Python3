# GUI编程
Python支持多种图形界面的第三方库，具体有：
1. Tk：图形库，支持多个操作系统，使用Tcl语言开发。     
2. wxWidgets
3. Qt
4. GTK
    
Python自带的Tkinter，已经支持Tk，因此可以直接使用。    

## Tkinter
Tkinter会调用本地的GUI接口，从而完成界面的绘制。     
在GUI中：    
1. 每一个Button/Label/Input都是一个Widget。     
2. Frame就是一个可以容纳Widget的Widget。    
`Widget.pack()`方法可以把当前Widget加入到上一级Widget中，并且实现简单的布局。    
`Frame.master`对象是最顶级的窗口，也就是主窗体。    
`Frame.mainloop()`方法就是让当前的整个应用窗体进行主消息循环。    

## 练习
1. 设计一个界面，输入框中输入用户的名称，点击打招呼按钮，可以弹出一个对话框，显示打招呼的信息。    
