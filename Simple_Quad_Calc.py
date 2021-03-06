version_num = ("1.0.A")
yes = ["y", 'yes', 'yee', 'ye', 'yah', 'yeah']
no = ["n", "no", "nah", "noda"]

print("Welcome to Quad. Calc. %s!" %version_num)
sv = int(input("1 for standard parabolas \n2 for vertex form parabolas \n1 or 2: "))

if sv == 1:
  print("From y = ax^2 + bx + c ...")
  a = int(input("a = "))
  b = int(input("b = "))
  c = int(input("c = "))
  if a == 0:
    print ("The given equation is linear, silly goose.\nUse point-slope or slope-intercept form.")
  else:
    new_H = int(b/a/2)
    new_K = int(c-a*b**2/4/a**2)
    check_abc = input("Are these values correct? ")
    if check_abc in yes:
      if a < 0:
        print("Vertex form: y = {aa}(x-{hh})^2 + {kk} \nCenter (h,k): ({hh},{kk})" .format (aa=a, hh=new_H,kk=new_K))
        print ("The parabola opens down.")
      elif a > 0:
        print("Vertex form: y = {aa}(x-{hh})^2 + {kk} \nCenter (h,k): ({hh},{kk})" .format (aa=a, hh=new_H,kk=new_K))
        print ("The parabola opens up.")  
    else:
      print ("Please re-enter the values")
      exit_ = input("Press any key to quit.")
      if exit_ != "":
        print("")
        
elif sv == 2:
  print("From y = a(x-h)^2 + k ...")
  a = int(input("a = "))
  h = int(input("h = "))
  k = int(input("k = "))
  new_B = int(0-2*a*h)
  new_C = int(k+a*h**2)
  check_abc = input("Are these values correct? ")
  if check_abc in yes:
    if a < 0:
      print ("The parabola opens down.")
      print("Center (h,k): ({hh},{kk}) \nStandard form: y = {aa}x^2 + {bb}x + {cc}" .format(hh=h, kk=k, aa=a, bb=new_B, cc=new_C))
    elif a > 0:
      print ("The parabola opens up.")
      print("Center (h,k): ({hh},{kk}) \nStandard form: y = {aa}x^2 + {bb}x + {cc}" .format(hh=h, kk=k, aa=a, bb=new_B, cc=new_C))
    elif a == 0:
      print ("The given equation is y = %d." %k)
  else:
    print ("Please re-enter the values")
    exit_ = input("Press any key to quit.")
    if exit_ != "":
      
      print("")
      
else:
  exit_ = input("Invalid entry - Press any key to quit.")
  if exit_ != "":
    print("")
