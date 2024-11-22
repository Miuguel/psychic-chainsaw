^!i:: ; Este é o atalho para Ctrl + Alt + I
    Send, {Text}Inwave3725 ;
    return
^!a:: ; Este é o atalho para Ctrl + Alt + A
    SendEvent, {Text}admin ; 
    return
^!e:: ; Este é o atalho para Ctrl + Alt + E
    SendRaw, ebfc5cee4d03d1 ;
    return
contador := 1

^!p::
    ; Formata o número com 2 dígitos (ex: 01, 02, etc.)
    
    numFormatado := Format("{:02}", contador)
    
    ; Envia o texto PDV seguido do número formatado
    SendEvent, {Text}PDV %numFormatado%
    contador++
    
return