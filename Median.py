import numpy as np

def median(array):
    N = array.shape[0]
    if N%2 == 0:
        return (array[(int(N/2))-1] + array[int((N/2)+1)-1]) / 2
    if N%2 != 0:
        return (array[int(N/2)])

def main():
    x = np.random.randint(1,100, size=11)
    x.sort()
    
    mean = round((sum(x)/x.shape[0]), 2)
    median_x = median(x)

    print(f'''{x}
Promedio: {mean}
Mediana: {median_x}
''')
    

if __name__ == '__main__':
    main() 
