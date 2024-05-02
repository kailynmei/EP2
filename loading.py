
import time
import sys

# PEGAMOS FUNÇÃO DO SITE DISPONIBILIZADO
def loading():
    total = 100
    for i in range(0, total + 1):
        time.sleep(0.03)  # Ajuste o valor para tornar o carregamento mais rápido
        percent = i * 100 // total
        filled_blocks = i * 50 // total
        empty_blocks = 50 - filled_blocks
        
        # Código ANSI para cor rosa de fundo e texto branco
        pink_bg = u"\u001b[45m"  # Rosa de fundo
        white_bg = u"\u001b[47m"  # Branco de fundo
        white_text = u"\u001b[37m"  # Texto branco
        reset_color = u"\u001b[0m"  # Resetar a cor
        
        loading_text = f"{pink_bg}{white_text}LOADING"
        dots = "." * (i // 20 % 4)  # Piscando os três pontos
        
        if i == total:
            progress_bar = f"{loading_text}{dots} {white_bg}{'█' * filled_blocks}{reset_color} {percent}%             "
        else:
            progress_bar = f"{loading_text}{dots} {pink_bg}{'█' * filled_blocks + ' ' * empty_blocks}{reset_color} {percent}%        "
        
        sys.stdout.write(u"\u001b[1000D")
        sys.stdout.write(progress_bar)
        sys.stdout.flush()
    
    print("\nSUCCESS!")
    time.sleep(1)