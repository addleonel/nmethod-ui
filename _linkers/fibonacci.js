function getSoma() {
    var {PythonShell} = require("python-shell")
    var path = require("path")


    var termo = document.getElementById("termo").value
    document.getElementById("termo").value = ""

    var output = "valor:"+termo;
    document.getElementById("are").innerHTML = output;
    
    var opcoes = {
        scriptPath : path.join(__dirname, '../_engine/'),
        args : [termo]
    }

    var somaFib = new PythonShell('newton.py', opcoes);

    somaFib.on('message', function(message) {
        // swal(message);
        swal("Listado de la iteración",message)
        
    })
    

    
}