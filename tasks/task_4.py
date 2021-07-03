tariff_info = {
   "root":{
      "children":[
         {
            "Внутрисетевой роуминг":{
               "children":[
                  {
                     "Internet":{
                        "children":[
                           "Значение A"
                        ]
                     }
                  },
                  {
                     "MMS":{
                        "children":[
                           "Входящие: 0.00",
                           "Исходящие: 6.45",
                           {
                              "Междугородние":{
                                 "children":[
                                    "Входящие: 0.00",
                                    {
                                       "Исходящие":{
                                          "children":[
                                             "Значение B"
                                          ]
                                       }
                                    }
                                 ]
                              }
                           },
                           {
                              "Местные":{
                                 "children":[
                                    "Входящие: 0.00"
                                 ]
                              }
                           }
                        ]
                     }
                  }
               ]
            }
         },
         {
            "Домашняя сеть":{
               "children":[
                  {
                     "Internet":{
                        "children":[
                           "Значение C"
                        ]
                     }
                  }
               ]
            }
         }
      ]
   }
}


def comf_read(tariff_info,rec=0):
    ind = ' '

    if isinstance(tariff_info,dict):
        for key,values in tariff_info.items():
            if key != 'children':
                print(ind * rec, key)
            comf_read(values,rec=rec+2)

    elif isinstance(tariff_info,list):
        for item in tariff_info:
            if isinstance(item,str):
                print(ind * rec, item)
            comf_read(item,rec=rec)


comf_read(tariff_info)

# root
#      Внутрисетевой роуминг
#          Internet
#              Значение A
#          MMS
#              Входящие: 0.00
#              Исходящие: 6.45
#              Междугородние
#                  Входящие: 0.00
#                  Исходящие
#                      Значение B
#              Местные
#                  Входящие: 0.00
#      Домашняя сеть
#          Internet
#              Значение C