^!i:: ; Este é o atalho para Ctrl + Alt + I
    SendEvent, {Text}Inwave3725 ;
    return
^!a:: ; Este é o atalho para Ctrl + Alt + A
    SendEvent, {Text}admin ; 
    return
^!e:: ; Este é o atalho para Ctrl + Alt + E
    SendEvent, {Text}ebMAC ; 
    return
contador := 0
^!p::
    ; Formata o número com 2 dígitos (ex: 01, 02, etc.)
    numFormatado := Format("{:02}", contador)
    
    ; Envia o texto PDV seguido do número formatado
    SendEvent, {Text}PDV %numFormatado%
    contador++
    
return