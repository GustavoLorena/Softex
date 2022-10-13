def funcao():
    opc = 1;
    while(True):
        opc = int(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n"));

        if (opc < 1 or opc > 4): break;

        print("\nPrimeiro número:\n");
        num_a = complex(input());
        print("\nSegundo número:\n");
        num_b = complex(input());
        print("\nTerceiro número:\n");
        num_c = complex(input());

        if(opc == 1):
            total = (num_a + num_b + num_c);
            print(total,"Propriedade Real: ", total.real,"Propriedade Imag: ",total.imag)
        elif(opc == 2):
            total = (num_a - num_b - num_c);
            print(total,"Propriedade Real: ", total.real,"Propriedade Imag: ",total.imag)
        elif(opc == 3):
            total = (num_a * num_b * num_c);
            print(total,"Propriedade Real: ", total.real,"Propriedade Imag: ",total.imag)
        elif(opc == 4):
            total = (num_a / num_b / num_c);
            print(total,"Propriedade Real: ", total.real,"Propriedade Imag: ",total.imag)

        print ("\n\n")

funcao();
