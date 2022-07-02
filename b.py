def main():
	orange_price = input("Enter price fruit : ") #giá bán của quả cam là bao nhiêu /kg
	fruit_weight = input("Enter weight of fruit : ") #khách muốn mua bao nhiêu kg
	money_given = input("Total money customer give you : ") #khách đưa cho bạn bao nhiêu tiền
	fruit_weight = float(fruit_weight)#đổi string thành float
	money_given = float(money_given)
	orange_price = float(orange_price)

	money_pay = total_money_pay(orange_price, fruit_weight)
	money_return = total_money_return(money_given, money_pay)

	print("fruit price : "+str(orange_price)) #in ra giá bán
	print("Total weight : "+str(fruit_weight))#in ra cân nặng
	print("Total money you given : "+str(money_given))#số tiền nhân viên nhận từ khách hàng
	print("Total money pay : "+str(money_pay))#số tiền khách hàng cần thanh toán
	if money_return == -1:
		print("Not enough cash!")
	else:	
		print("Total money return : "+str(money_return))
	money_info(money_return)
	
#code trả lại kết quả tiền cần trả khách
def total_money_pay(orange_price, fruit_weight):
	return orange_price*fruit_weight
def total_money_return(money_given, money_pay):
	if money_given < money_pay:
		return -1
	return money_given-money_pay

#code tính số tờ tiền cần trả
def money_info(money_return):
	count_500 = money_return/500
	count_500 = int(count_500)
	left_over = money_return-500*count_500
	print("\n500k : "+str(count_500))

	count_200 = int(left_over/200)
	left_over = left_over-200*count_200
	print("200k : "+str(count_200))

	count_100 = int(left_over/100)
	left_over = left_over-100*count_100
	print("100k : "+str(count_100))

	count_50 = int(left_over/50)
	left_over = left_over-50*count_50
	print("50k : "+str(count_50))

	count_20 = int(left_over/20)
	left_over = left_over-20*count_20
	print("20k : "+str(count_20))

	count_10 = int(left_over/10)
	left_over = left_over-10*count_10
	print("10k : "+str(count_10))

	count_5 = int(left_over/5)
	left_over = left_over-5*count_5
	print("5k : "+str(count_5))

	count_2 = int(left_over/2)
	left_over = left_over-2*count_2
	print("2k : "+str(count_2))

	count_1 = int(left_over/1)
	left_over = left_over-1*count_1
	print("1k : "+str(count_1))

main()
