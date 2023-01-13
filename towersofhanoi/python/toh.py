def hanoi(numOfDisks, src, aux, dest):
    if numOfDisks == 1:
        print(f'Move disk 1 from {src} to {dest}')
        return
    hanoi(numOfDisks - 1, src, dest, aux)
    print(f'Move disk {numOfDisks} from {src} to {dest}')
    hanoi(numOfDisks - 1, aux, src, dest)

hanoi(4, '1', '2', '3')
