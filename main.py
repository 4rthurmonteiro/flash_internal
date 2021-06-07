################################################################################
# iflash
#
# Created: 2016-03-22 15:54:21.232663
#
################################################################################

import streams
import json
import flash
import mcu

streams.serial()

quantity_size_bytes = 10
quantity_address = 3211264
quantity = -1
element_size_bytes = 34

# def quantity_address():
#     return format(3211264, '#04x')

def start_address_to_save(number_of_items_saved: int):
    initial_address = 3211264
    quantity_size = 10
    package_max_size = 34

    return (initial_address + quantity_size) + (package_max_size * number_of_items_saved)


    
# print(quantity_address == 0x00310000)    
print('---------- iniciando programa ---------------')

sleep(1000)

while quantity < 6:

    print('Primeiro vamos consultar a quantidade de tuplas salvas:')
    

    
    ff = flash.FlashFileStream(quantity_address, quantity_size_bytes)
    ff.seek(0,streams.SEEK_SET)
    
    n = ff.read_int()
    # ff.flush()
    ff.close()
    
    sleep(1000)

    if n > 10:
        print('Quantidade ainda nao iniciada (n igual a', n ,') vamos iniciar...')
        ff = flash.FlashFileStream(quantity_address, quantity_size_bytes)
        quantity_tuple = (0,)
        quantity_ds = json.dumps(quantity_tuple)
        ff.write(len(quantity_ds))
        ff.write(quantity_ds)
        ff.flush()
        ff.seek(0,streams.SEEK_SET)
        new_n = ff.read_int()
        print('new n igual a => ', new_n )
        paramsb = bytearray()                       # create an array to hold flash
        for i in range(4,new_n+4):                     # copy to array from flash
            paramsb.append( ff[i]  )
        paramss = str( paramsb )                        # convert to a string 
        paramsj = json.loads( paramss )   
        print('ds after decode',paramsj) # convert to JSON
        quantity = paramsj[0]
    
        ff.close()
        sleep(1000)

        # mcu.reset()
        
    else:
        ff = flash.FlashFileStream(quantity_address, quantity_size_bytes)
        ff.seek(0,streams.SEEK_SET)
        old_n = ff.read_int()
        print('old n igual a => ', old_n )
        paramsb = bytearray()                       # create an array to hold flash
        for i in range(4,n+4):                     # copy to array from flash
            paramsb.append( ff[i]  )
        paramss = str( paramsb )                        # convert to a string 
        paramsj = json.loads( paramss )   
        print('ds after decode',paramsj)
        quantity = paramsj[0]
        ff.close()
        sleep(1000)

        
    print('quantidade => ',quantity)   
    
    print('--------- Temos a quantidade salva, agora vamos salvar de no prox espaco livre ---------')
    
    # esse valor vira dos sensores e do calculo da hora
    t = (
      439,
      100,
      279,
      0,
      1623024306879
    )
    
    ds = json.dumps(t)
    
    print('ds before save in buffer =>', ds)
    print('ds len before save in buffer =>', len(ds))
    
    ff = flash.FlashFileStream(start_address_to_save(quantity), element_size_bytes)
    
    
    # save length and json to flash
    ff.write(len(ds))
    ff.write(ds)
    
    ff.flush()
    
    ff.seek(0, streams.SEEK_SET)
    
    print("reading flash file")
    
    n_2 = ff.read_int()
    
    
    
    print('n_2 after save in buffer =>', n_2)
    
    # do a few checks on validity of size which I have omitted
    paramsb = bytearray()                       # create an array to hold flash
    for i in range(4,n_2+4):                     # copy to array from flash
        paramsb.append( ff[i]  )
    paramss = str( paramsb )                        # convert to a string 
    paramsj = json.loads( paramss )                 # convert to JSON
    
    
    print('ds after decode',paramsj)
    
    ff.close()
    sleep(1000)
    
    
    if 32 > n_2 > 28:
    
        print('-------- agora vamos atualizar a quantidade --------')
        
        quantity = quantity + 1
        
        ff = flash.FlashFileStream(quantity_address, quantity_size_bytes)
        
        quantity_tuple = (quantity,)
        
        quantity_ds = json.dumps(quantity_tuple)
        ff.write(len(quantity_ds))
        ff.write(quantity_ds)
        ff.flush()
        ff.close()        
    

print('--------- vamos ler os dados salvos --------')

counter = 0 

while counter != quantity:
    ff = flash.FlashFileStream(start_address_to_save(counter), element_size_bytes)
    counter = counter + 1
    
    print("reading flash file")
    ff.seek(0, streams.SEEK_SET)
    n_3 = ff.read_int()
    
    
    
    print('n_3 after save in buffer =>', n_3)
    
    # # do a few checks on validity of size which I have omitted
    # paramsb = bytearray()                       # create an array to hold flash
    # for i in range(4,n_3+4):                     # copy to array from flash
    #     paramsb.append( ff[i]  )
    # paramss = str( paramsb )                        # convert to a string 
    # paramsj = json.loads( paramss )                 # convert to JSON
    
    
    # print('ds after decode',paramsj)
    
    ff.close()
    sleep(1000)
    

    
    




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