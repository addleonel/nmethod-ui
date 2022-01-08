function get_falseposition(){
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var valor_a = document.getElementById("valor_a").value
    var valor_b = document.getElementById("valor_b").value

    document.getElementById("valor_a").value = ""
    document.getElementById("valor_b").value = ""

    var output = "Intervalo: ["+valor_a+";"+valor_b+"]";
    document.getElementById("are").innerHTML = output;
    swal(output);

    var opcoes = {
        scriptPath: path.join(__dirname, '../_engine/'),
        args: [valor_a, valor_b]
    }

    var imc = new PythonShell('false-positionMethod.py', opcoes)

    imc.on("message", function(message){
        swal("La iteración ",message)
    })
}