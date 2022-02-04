
var inputs = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener('click', AddValor);
}


function AddValor() {
  var resultado = parseFloat(this.value, 10);
  var principal = document.getElementById('valor_principal');
  var total = parseFloat(principal.value, 10);

  this.checked == true ? total += resultado : total -= resultado;

  principal.value = total;
}

var clicked = false;
$(".checkall").on("click", function() {
  $(".checkhour").prop("checked", !clicked);
  clicked = !clicked;
});


$(document).ready(function(){
    $("#btn1").click(function(acerto){
      $("#acerto").html(5);
    });
    $("#btn2").click(function(erro){
      $("#erro").html(-3);
    });

  });

  $(document).ready(function(){
    $(".check").click(function(){
        $("#evento_value2").prop("checked", true);
    });
    $(".uncheck").click(function(){
        $("#myCheck").prop("checked", false);
    });
});




if (localStorage.acerto) {
	document.getElementById('acerto').value = localStorage.acerto;
}
if (localStorage.erro) {
	document.getElementById('erro').value = localStorage.erro;
}



var salvarPontos = function() {
	var acerto = document.getElementById('acerto').value;
	var erro = document.getElementById('erro').value;

	localStorage.setItem('acerto', acerto);
	localStorage.setItem('erro', erro);
	
};

document.onchange = salvarData;



