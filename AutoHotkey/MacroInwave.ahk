^!i:: ; Este é o atalho para Ctrl + Alt + I
    Send, {Text}password ;
    return
^!a:: ; Este é o atalho para Ctrl + Alt + A
    SendEvent, {Text}user ; 
    return
^!e:: ; Este é o atalho para Ctrl + Alt + E
    SendRaw, serverPassword ;
    return
contador := 1

^!p::
    ; Formata o número com 2 dígitos (ex: 01, 02, etc.)
    
    numFormatado := Format("{:02}", contador)
    
    ; Envia o texto PDV seguido do número formatado
    SendEvent, {Text}PDV %numFormatado%
    contador++
    
return
