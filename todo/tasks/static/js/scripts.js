//Criando janela de confirmação antes da deleção de uma tarefa.
$(document).ready(function() {
    
    var deleteBtn = $('.delete-btn');

    $(deleteBtn).on('click', function(e){

        e.preventDefault();     
    

    var delLink = $(this).attr('href');
    var result = confirm('Deseja realmente excuir a tarefa?');

    if(result) {
        window.location.href = delLink;
    }

})

});


