print("\033c\033[43;30m\nboard\n")

# corrigido: cada dimensão é independente
def board4d(x,y,z,t):
    return [[[[" " for _ in range(x)] for _ in range(y)] for _ in range(z)]for _ in range(t)]

a=board4d(2,2,2,2)
a[0][0][0]="X"
a[0][0][1]="O"
print(a)