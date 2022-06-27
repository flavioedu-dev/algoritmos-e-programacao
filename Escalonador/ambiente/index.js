/* Função para organizar os processos de acordo com o tempo de processamento */
function mudarPosition(arr, from, to){
    
    arr.splice(to, 0, arr.splice(from, 1)[0])

    return arr
}

/* Função que atribui o delay */
const timer = (seconds) =>  {
    let time = seconds * 1000
    return new Promise(res => setTimeout(res, time))
}

/* Filas de processos cada uma com seu algoritmo interno */
let sistema = [ /* FIFO - (Prioridade Alta)*/
    {
        name: "explorer",
        time: 1
    },
    {
        name: "processando imagem",
        time: 3
    },
    {
        name: "carregando dados",
        time: 2
    }
]

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

let batch = [ /* RR - Circular (Prioridade Baixa) */
    {
        name: "process 1",
        time: 3
    },
    {
        name: "process 2",
        time: 3
    },
    {
        name: "process 3",
        time: 3
    }
]


/* Laço para a ordenar os processos da fila com o SJT */
for (let i=0; i<interativos.length; i++){
    
    if (i>0){

        for (let j=0; j <= i; j++){

            if (interativos[i].time < interativos[j].time){
    
                mudarPosition(interativos, i, j)
    
            }

        }

    }

}


/* Funções para a exibição dos processos */
async function exibirSistema(){
    console.log("---- Executando fila 0 | FIFO ----")
    for (let i=0; i<sistema.length; i++){
    
        console.log(`Sistema: ${sistema[i].name} / tempo de execução: ${sistema[i].time}`)
        await timer(2)
    }
    console.log("~~~ Fila 0 concluída ~~~")
    console.log("   ")
    await timer(1)
}


async function exibirInterativos(){
    console.log("---- Executando fila 1 | SJF ----")
    for (let i=0; i<interativos.length; i++){

        console.log(`Interativos: ${interativos[i].name}  / tempo de execução: ${interativos[i].time}`)
        await timer(2)

    }
    console.log("~~~ Fila 1 concluída ~~~")
    console.log("   ")
    await timer(1)
}

async function exibirBatch(){
    console.log("---- Executando fila 2 | RR ----")

    for (let i=0; i<batch.length; i++){

        console.log(`Batch: ${batch[i].name}   / tempo de execução: ${batch[i].time}`)
        await timer(1)

    }
    for (let i=0; i<batch.length; i++){

        console.log(`Batch: ${batch[i].name}   / tempo de execução: ${batch[i].time}`)
        await timer(1)

    }
    for (let i=0; i<batch.length; i++){

        console.log(`Batch: ${batch[i].name}   / tempo de execução: ${batch[i].time}`)
        await timer(1)

    }
    console.log("~~~ Fila 2 concluída ~~~")
    console.log("   ")
    await timer(1)
}

/* Função para controlar a exibição dos processos*/
async function executar(){
    await exibirSistema()
    await exibirInterativos()
    exibirBatch()
}

executar()