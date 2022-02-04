(function() 
 {
  var allQuestions = [{
    question: "Quando o funcionário precisar entrar na câmara fria qual é a primeira coisa que ele precisa fazer?",
    options: ["a) Ir até o armário e colocar o kit completo de EPI.", "b) Saber onde os produtos estão localizados lá dentro.",],
    answer: 0
  }, {
    question: "Após vestir os EPIs o que você deve fazer para acessar as câmaras frias?",
    options: ["a) Entrar imediatamente nas câmaras frias.", " b) Fazer o seu registro de entrada."],
    answer: 1
  }, {
    question: "Para realizar o registro de entrada é necessário ser de forma eletrônica, seja para registrar a entrada ou a saída. Se caso você for registrar a sua entrada nas câmaras frias e não tiver como ser de forma eletrônica como proceder?",
    options: [" a) Entrar mesmo sem o registro, pois é prioridade fazer o trabalho.", " b) Procurar um formulário impresso para o seu registro de entrada"],
    answer: 1
  },{
    question: "Quais informações são necessárias para o registro de acesso, tanto o manual em formulário quanto eletrônico?",
    options: ["a) O nome, a sala aonde o funcionário vai, a data e hora de entrada e saída.", "b) O nome e o RG do funcionário."],
    answer: 0
  }, {
    question: "Existe um tempo máximo que o funcionário pode ficar dentro das câmaras frias. Como saber que tempo é esse?",
    options: [" a) Existem placas com o aviso nas portas das câmaras indicando o tempo de permanência em cada uma.", " b) o funcionário fica quanto tempo ele precisar."],
    answer: 1
  },{
    question: "Qual é o tempo de permanência nas câmaras de resfriados?",
    options: [" a) 1:40 hrs. Uma hora e quarenta minutos.", "b) 5:00 hrs. Cinco horas."],
    answer: 0
  },{
    question: "Qual é o tempo de permanência nas câmaras de congelados?",
    options: [" a) 1:00 hrs. Uma hora.", "b) 2:00 hrs. duas horas."],
    answer: 0
  },{
    question: "Já sabemos que existe um tempo máximo de permanência dentro das câmaras e é preciso de um tempo para fazer uma recuperação térmica. A recuperação térmica é feita dentro das Câmaras Frias?",
    options: [" a) Sim", " b) Não"],
    answer: 1
  },{
    question: "Quais os tempos de recuperação térmica que devem ser respeitados após sua saída nas câmaras?",
    options: ["a) Câmara Resfriada 20 min. Câmara Congelada 1 hora.", "b) Câmara Resfriada 1h. Câmara Congelada 2h."],
    answer: 1
  },{
    question: "O seu registro de entrada foi feito pela planilha impressa ou pelo registro eletrônico. Agora para você sair, também é preciso fazer o registro de saída?",
    options: [" a) Sim, é necessário fazer o registro de entrada e o de saída também.", " b) Não, o registro é só para entrada."],
    answer: 0
    }];
  
  var quesCounter = 0;
  var selectOptions = [];
  var quizSpace = $('#quiz');
    
  nextQuestion();
    
  $('#next').click(function () 
    {
        chooseOption();
        if (isNaN(selectOptions[quesCounter])) 
        {
            alert('Por favor escolha uma das respostas!');
        } 
        else 
        {
          quesCounter++;
          nextQuestion();
        }
    });
  
  $('#prev').click(function () 
    {
        chooseOption();
        quesCounter--;
        nextQuestion();
    });
  
  function createElement(index) 
    {
        var element = $('<div>',{id: 'question'});
        var header = $('<h2>Fase: 0' + (index + 1) + ' :</h2>');
        element.append(header);

        var question = $('<p>').append(allQuestions[index].question);
        element.append(question);

        var radio = radioButtons(index);
        element.append(radio);

        return element;
    }
  
  function radioButtons(index) 
    {
        var radioItems = $('<ul>');
        var item;
        var input = '';
        for (var i = 0; i < allQuestions[index].options.length; i++) {
          item = $('<li>');
          input = '<input type="radio" name="answer" value=' + i + ' />';
          input += allQuestions[index].options[i];
          item.append(input);
          radioItems.append(item);
        }
        return radioItems;
  }
  
  function chooseOption() 
    {
        selectOptions[quesCounter] = +$('input[name="answer"]:checked').val();
    }
   
  function nextQuestion() 
    {
        quizSpace.fadeOut(function() 
            {
              $('#question').remove();
              if(quesCounter < allQuestions.length)
                {
                    var nextQuestion = createElement(quesCounter);
                    quizSpace.append(nextQuestion).fadeIn();
                    if (!(isNaN(selectOptions[quesCounter]))) 
                    {
                      $('input[value='+selectOptions[quesCounter]+']').prop('checked', true);
                      
                    }
                    if(quesCounter === 1)
                    {
                      
                      $('#prev').show();
                    } 
                    else if(quesCounter === 0)
                    {
                      $('#prev').hide();
                      $('#next').show();
                    }
                }
              else 
                {
                    var scoreRslt = displayResult();
                    quizSpace.append(scoreRslt).fadeIn();
                    $('#next').hide();
                    $('#prev').hide();
                }
        });
    }
  
  function displayResult() 
    {
        var score = $('<p>',{id: 'question'});
        var correct = 0;
        for (var i = 0; i < selectOptions.length; i++) 
        {
          if (selectOptions[i] === allQuestions[i].answer) 
          {
            correct++;
            
          }
        }
        score.append('Parabens, você acertou ' + correct + ' de ' +allQuestions.length);
        return score;
  }
})();