import numpy as np 
import matplotlib.pyplot as plt 
 
def main(): 
	N = 4 
	ind = np.arange(N)  # 获得 x 轴的坐标序列 
	width = 0.2       # the width of the bars
	fig, ax = plt.subplots() # 得到图表 
	rects = []
	grade = ((540, 517, 485, 503), (488, 461, 435, 452), (368, 331, 330, 342)) 
	
	#分别构造单个序列的数据对应的图形，并设置颜色 
	rects.append(ax.bar(ind + width * 1, grade[0], width, color = 'red')) 
	rects.append(ax.bar(ind + width * 2, grade[1], width, color = 'blue'))
	rects.append(ax.bar(ind + width * 3, grade[2], width, color = 'green'))
	ax.set_ylabel('Grade') # 设置坐标轴标题  
	ax.set_title('Grade analysis') 
	ax.set_xticks(ind + 2.5 * width) 
	ax.set_xticklabels(('2011', '2012', '2013', '2014')) 
	ax.legend((rects[0],rects[1],rects[2]),("Level 1","Level 2","Level 3"))# 绘制图形（柱状图和图例）
	def autolabel(rects):# 定义函数，在每一个序列的柱形图上显示数值 
        # attach some text labels 
		for rect in rects: 
			height =rect.get_height()# 获得每一列的高度值 
			ax.text(rect.get_x()+rect.get_width()/2.,1.00*height,"%d"%int(height),ha="center",va="bottom")# 显示数值，并设定其显示位置 
	for i  in range(0, 3): 
		autolabel(rects[i])# 调用函数，给每一列显示数值 
	plt.show()                             # 显示图形 
 
if __name__ == '__main__': 
	main()
