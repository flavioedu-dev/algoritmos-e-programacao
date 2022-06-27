let interativos = [ /* SJF - Menor tempo de execução - (Prioridade Média) */
    {
        name: "mouseenter",
        time: 3
    },
    {
        name: "I/O bound",
        time: 10
    },
    {
        name: "click",
        time: 4
    },
    {
        name: "mouseover",
        time: 5
    }
]

function mudarPosition(arr, from, to){
    
    arr.splice(to, 0, arr.splice(from, 1)[0])

    return arr
}

/* console.log(interativos) */
let menor = 0
let cont = 1

for (let i=0; i<interativos.length; i++){

    if (i == 0){
        menor = interativos[i].time
        /* console.log(menor) */
    }
    
    if (i>0){

        for (let j=0; j <= i; j++){
            console.log(j)

            if (interativos[i].time < interativos[j].time){
                /* i=2, click[1] - I/O bound[2] // i=4,  mouseover[2]- I/O bound[3] */
                /* j=2, click[1] - I/O bound[2] // j=3,  mouseover[2]- I/O bound[3] */
    
                mudarPosition(interativos, i, j)
    
            }

        }
        
    }
}
console.log(interativos)