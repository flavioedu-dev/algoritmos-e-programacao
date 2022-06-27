let interativos = [ /* SJF - Menor tempo de execução - (Prioridade Média) */
    {
        name: "mouseenter",
        time: 2
    },
    {
        name: "I/O bound",
        time: 5
    },
    {
        name: "click",
        time: 0
    },
    {
        name: "mouseover",
        time: 1
    }
]

function mudarPosition(arr, from, to){
    
    arr.splice(to, 0, arr.splice(from, 1)[0])

    return arr
}

console.log(interativos)
let menor = 0

for (let i=0; i<interativos.length; i++){

    if (i == 0){
        menor = interativos[i].time
        /* console.log(menor) */
    }
    
    if (i>0){

        for (j in interativos){

            if (interativos[j].time < interativos[i-1].time){
                /* i=3, click[1] - I/O bound[2] // i=4,  mouseover[2]- I/O bound[3] */
                /* j=2, click[1] - I/O bound[2] // j=3,  mouseover[2]- I/O bound[3] */
                

                /* console.log(j)
                console.log(j-1) */


                mudarPosition(interativos, i, i-1)

            }
        }
        /* while (interativos[i].time < menor){


            mudarPosition(interativos, i, 0)
        } */

    }

}

console.log(interativos)
