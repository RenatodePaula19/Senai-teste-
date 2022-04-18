function habilita_botao(){
    var status = document.getElementById('status').innerHTML 
    alert(status)
    


    if (status.trim() =='Fechado'){
        alert('ENTROU')
        document.getElementsByClassName('botao').disabled = true
    }
}