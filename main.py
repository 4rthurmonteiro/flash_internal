import streams
import json
import flash

streams.serial()

quantity_size_bytes = 32
quantity_address = 3211264
quantity = -1
element_size_bytes = 34
quantity_max_bytes = 10


def start_address_to_save(number_of_items_saved: int):
    initial_address = 3211264
    quantity_size = 32
    package_max_size = 34

    result =  (initial_address + quantity_size) + (package_max_size * number_of_items_saved)
    
    print('start_address_to_save =>', hex(result))
    
    return result

def check_address_bytes(start_address, size_bytes):
    ff = flash.FlashFileStream(start_address, size_bytes)
    ff.seek(0,streams.SEEK_SET)
    
    n = ff.read_int()
    # ff.flush()
    ff.close()
    
    print('check_bytes => return is ', n)
    
    return n
    
    
def find_by_address_bytes(start_address, size_bytes):
    ff = flash.FlashFileStream(start_address, size_bytes)
    ff.seek(0,streams.SEEK_SET)
    
    n = ff.read_int()
    print('find_by_address_bytes => bytes value is ', n)

    paramsb = bytearray()                       # create an array to hold flash
    for i in range(4,n+4):                     # copy to array from flash
        paramsb.append( ff[i]  )
    paramss = str( paramsb )                        # convert to a string 
    paramsj = json.loads( paramss )   
    
    ff.close()
    
    print('find_by_address_bytes => return is ', paramsj)
    
    return paramsj    
    
def write_value(json, start_address, size):
    ff = flash.FlashFileStream(start_address, size)
    ll_1 = ff.write(len(json))
    ll_2 = ff.write(json)
    ff.flush()
    ff.close()
    
    print('write_value => return len object: ', ll_1, ' return object:', ll_2)
    
    
print('---------- iniciando programa ---------------')

############### so pra zerar a quantidade
quantity_tuple = (0,)
write_value(json.dumps(quantity_tuple), quantity_address, quantity_size_bytes)
find_by_address_bytes(quantity_address, quantity_size_bytes)

sleep(1000)

# while quantity < 2:

print('Primeiro vamos consultar a quantidade de tuplas salvas:')

quantity_bytes = check_address_bytes(quantity_address, quantity_size_bytes)

sleep(1000)

if quantity_bytes > quantity_max_bytes:
    quantity = 0
    quantity_tuple = (quantity,)
    write_value(json.dumps(quantity_tuple), quantity_address, quantity_size_bytes)

    sleep(1000)
else:
    quantity_tuple = find_by_address_bytes(quantity_address, quantity_size_bytes)
    quantity = quantity_tuple[0]
    sleep(1000)

        
print('quantidade => ',quantity)   
    
print('--------- Temos a quantidade salva, agora vamos salvar de no prox espaco livre ---------')
#     # print('mockando a quantidade sempre zer')

# for n in range(20):
t = (
  439,
  100,
  279,
  0,
  1623024306879
)

write_value(json.dumps(t), start_address_to_save(quantity), element_size_bytes)
find_by_address_bytes(start_address_to_save(quantity), element_size_bytes)    

print('---- update quantity ----')

quantity = quantity + 1

print('---- update quantity ----,  ', quantity, ' --- ')


# quantity_tuple = (quantity,)
# write_value(json.dumps(quantity_tuple), quantity_address, quantity_size_bytes)
# find_by_address_bytes(quantity_address, quantity_size_bytes)
    
# write_value(json.dumps(t), start_address_to_save(quantity), element_size_bytes)
# find_by_address_bytes(start_address_to_save(quantity), element_size_bytes)    

# print('---- update quantity ----')

# quantity = quantity + 1

# print('---- update quantity ----,  ', quantity, ' --- ')


# quantity_tuple = (quantity,)
# write_value(json.dumps(quantity_tuple), quantity_address, quantity_size_bytes)
# find_by_address_bytes(quantity_address, quantity_size_bytes)    
    


# # write_value(json.dumps(t), start_address_to_save(15), element_size_bytes)
# find_by_address_bytes(start_address_to_save(1), element_size_bytes)    
# esse valor vira dos sensores e do calculo da hora
# t = (
#   439,
#   100,
#   279,
#   0,
#   1623024306879
# )

# write_value(json.dumps(t), start_address_to_save(quantity), element_size_bytes)
# find_by_address_bytes(start_address_to_save(quantity), element_size_bytes)    

# print('---- update quantity ----')

# quantity = quantity + 1

# quantity_tuple = (quantity,)
# write_value(json.dumps(quantity_tuple), quantity_address, quantity_size_bytes)
# find_by_address_bytes(quantity_address, quantity_size_bytes)

# t = (
#   501,
#   100,
#   279,
#   0,
#   1623024306879
# )

# write_value(json.dumps(t), start_address_to_save(quantity), element_size_bytes)
# find_by_address_bytes(start_address_to_save(quantity), element_size_bytes)  

# t = (
#   501,
#   100,
#   279,
#   0,
#   1623024306879
# )

write_value(json.dumps(t), start_address_to_save(2), element_size_bytes)
find_by_address_bytes(start_address_to_save(2), element_size_bytes)  

write_value(json.dumps(t), start_address_to_save(3), element_size_bytes)
find_by_address_bytes(start_address_to_save(3), element_size_bytes)  

write_value(json.dumps(t), start_address_to_save(4), element_size_bytes)
find_by_address_bytes(start_address_to_save(4), element_size_bytes)  

write_value(json.dumps(t), start_address_to_save(5), element_size_bytes)
find_by_address_bytes(start_address_to_save(5), element_size_bytes)  

write_value(json.dumps(t), start_address_to_save(6), element_size_bytes)
find_by_address_bytes(start_address_to_save(6), element_size_bytes)  

# print('-------- vamos tentar ler os dados -------')
# # find_by_address_bytes(start_address_to_save(0), element_size_bytes)  
# # find_by_address_bytes(start_address_to_save(0), element_size_bytes)  

# find_by_address_bytes(start_address_to_save(1), element_size_bytes)  
# find_by_address_bytes(start_address_to_save(2), element_size_bytes)  
find_by_address_bytes(start_address_to_save(3), element_size_bytes)  
find_by_address_bytes(start_address_to_save(4), element_size_bytes)  
find_by_address_bytes(start_address_to_save(5), element_size_bytes)  
find_by_address_bytes(start_address_to_save(6), element_size_bytes)  


# for n in range(2, 40):
#     find_by_address_bytes(start_address_to_save(n), element_size_bytes)  

# find_by_address_bytes(start_address_to_save(1), element_size_bytes)  

# for q in range(quantity+1):
#     print(q)
#     find_by_address_bytes(start_address_to_save(q), element_size_bytes)  
# find_by_address_bytes(0x00310284, element_size_bytes)  





#     sleep(1000)
    
#     print('--- checando novamente')
    
#     ff = flash.FlashFileStream(start_address_to_save(quantity), element_size_bytes)
#     ff.seek(0,streams.SEEK_SET)

#     n_10 = ff.read_int()
#     print(n_10)
    
#     paramsb = bytearray()                       # create an array to hold flash
#     for i in range(4,n_10+4):                     # copy to array from flash
#         paramsb.append( ff[i]  )
#     paramss = str( paramsb )                        # convert to a string 
#     paramsj = json.loads( paramss )                 # convert to JSON
    
    
#     print('n_10 ds after decode',paramsj)
    
#     ff.close()
    # if 32 > n_2 > 28:
    
    #     print('-------- agora vamos atualizar a quantidade --------')
        
    #     quantity = quantity + 1
        
    #     ff = flash.FlashFileStream(quantity_address, quantity_size_bytes)
        
    #     quantity_tuple = (quantity,)
        
    #     quantity_ds = json.dumps(quantity_tuple)
    #     ff.write(len(quantity_ds))
    #     ff.write(quantity_ds)
    #     ff.flush()
    #     ff.close()        
    

# print('--------- vamos ler os dados salvos --------')

# counter = 0 

# while counter != quantity:
#     ff = flash.FlashFileStream(start_address_to_save(counter), element_size_bytes)
#     counter = counter + 1
    
#     print("reading flash file")
#     ff.seek(0, streams.SEEK_SET)
#     n_3 = ff.read_int()
    
    
    
#     print('n_3 after save in buffer =>', n_3)
    
#     # # do a few checks on validity of size which I have omitted
#     # paramsb = bytearray()                       # create an array to hold flash
#     # for i in range(4,n_3+4):                     # copy to array from flash
#     #     paramsb.append( ff[i]  )
#     # paramss = str( paramsb )                        # convert to a string 
#     # paramsj = json.loads( paramss )                 # convert to JSON
    
    
#     # print('ds after decode',paramsj)
    
#     ff.close()
#     sleep(1000)
    

    
    




# print('agora vamos salvar a quantidade')


# ff_2 = flash.FlashFileStream(0x00310000,181)

# ff_2.seek(0, streams.SEEK_SET)

# n_2 = ff_2.read_int()


# paramsb_2 = bytearray()                       # create an array to hold flash
# for i in range(4,n_2+4):                     # copy to array from flash
#     paramsb_2.append( ff_2[i]  )
# paramss_2 = str( paramsb_2 )                        # convert to a string 
# paramsj_2 = json.loads( paramss_2 )                 # convert to JSON

# print('n_2 after save in buffer =>', n_2)

# print('ds after decode ****',paramsj_2)