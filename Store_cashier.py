import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("صندوق  فروشگاهی")

#دیکشنری محصولات
products={
    "شیر" : 20000,
    "نان" : 15000,
    "آب معدنی" : 10000,
    "شکلات" : 35000,
    "بستنی" : 25000,
    "نوشابه" : 30000,
    "سبزیجات" : 40000,
    "آب میوه" : 20000,
    "پاستیل" : 22000,
    "کیک" : 17000,
    "آدامس" : 19000
}
cart = []

#تابع جستجوی محصول و نمایش قیمت
def search_product(product_name):
    if product_name in products:
        price_label.config(text=f"قیمت: {products[product_name]} تومان")
    else:
        messagebox.showerror(text="محصول یافت نشد")


#تابع افزودن به سبد خرید
def add_to_cart(product_name):
    if product_name in products:
        cart.append(product_name)
        update_cart_display()
        update_total_price()
    else:
        messagebox.showerror("محصول وارد شده معتبر نیست:", product_name)

#تابع حذف محصول از سبد خرید      
def remove_from_cart(product_name):
    if product_name in cart:
        cart.remove(product_name)
        update_cart_display()
        update_total_price()
    else:
        messagebox.showerror("محصول وارد شده برای حذف در سبد موجود نیست:", product_name)

#تابع به‌روزرسانی مجموع قیمت
def update_total_price():
    total = sum(products[item] for item in cart)
    total_price.config(text=f"مجموع قیمت خرید: {total} تومان")

#نمایش سبد خرید
def update_cart_display():
    cart_display.config(text="سبد خرید:\n" + "\n".join(cart))

#نمایش فاکتور نهایی
def show_invoice():
   receipt = "\n".join([f"{item} - {products[item]} تومان" for item in cart])
   messagebox.showinfo("فاکتور خرید", f"{receipt}\n\n مجموع مبلغ: {sum(products[item] for item in cart)} نومان")

#نمایش لیست محصولات موجود
products_display = tk.Label(root , text="محصولات موجود:\n" + "\n".join([f"{name} - {price} تومان" for name, price in products.items()]), justify="left")
products_display.pack()

#فیلد ورودی برای نام محصول
entry = tk.Entry(root)
entry.pack()

#دکمه‌ی جستجو
search_button = tk.Button(root, text="جستجوی محصول", command=search_product)
search_button.pack()

#نمایش قیمت محصول
price_label = tk.Label(root, text="قیمت: ")
price_label.pack()

#دکمه‌ی افزودن به سبد خرید
add_button = tk.Button(root, text="افزودن به سبد خرید", command=add_to_cart)
add_button.pack()

#دکمه‌ی حذف محصول از سبد خرید
remove_button = tk.Button(root, text="حذف محصول از سبد خرید", command=remove_from_cart)
remove_button.pack()

#نمایش لیست سبد خرید
cart_display = tk.Label(root, text="سبد خرید:")
cart_display.pack()

#نمایش مجموع قیمت‌ها
total_price = tk.Label(root, text="مجموع قیمت:0 تومان")
total_price.pack()

#دکمه‌ی نمایش فاکتور
invoice_button = tk.Button(root, text="نمایش فاکتور", command=show_invoice)
invoice_button.pack()

#نمایش فاکتور نهایی
invoice_label = tk.Label(root, text="فاکتور:")
invoice_label.pack()

#اجرای برنامه
root.mainloop()