// Obtener los elementos de imagen de origen por sus identificadores
var sourceImage1 = document.querySelector("#source-image-1");
var sourceImage2 = document.querySelector("#source-image-2");
var sourceImage3 = document.querySelector("#source-image-3");
var sourceImage4 = document.querySelector("#source-image-4");
var circleProgressBar1 = document.querySelector("#progress-bar-circle-1");
var circleProgressBar2 = document.querySelector("#progress-bar-circle-2");
var circleProgressBar3 = document.querySelector("#progress-bar-circle-3");
// Obtener el elemento de imagen de destino por su identificador
var destinationImage = document.querySelector("#destination-image");


var progressValue1 = document.querySelector("#progress-value-1");
var progressValue2 = document.querySelector("#progress-value-2");
var progressValue3 = document.querySelector("#progress-value-3");






// Agregar un controlador de eventos de clic al primer elemento de imagen de origen
sourceImage1.addEventListener("click", function() {
  var sourceImageUrl = sourceImage1.src;
  destinationImage.src = sourceImageUrl;
  updateProgressValue(progressValue1, 30);
  updateProgressValue(progressValue2, 30);
  updateProgressValue(progressValue3, 50);
  updateDataValue(circleProgressBar1, 0.30);
  updateDataValue(circleProgressBar2, 0.30);
  updateDataValue(circleProgressBar3, 0.50);
});

// Agregar un controlador de eventos de clic al segundo elemento de imagen de origen
sourceImage2.addEventListener("click", function() {
  var sourceImageUrl = sourceImage2.src;
  destinationImage.src = sourceImageUrl;
  updateProgressValue(progressValue1, 50);
  updateProgressValue(progressValue2, 25);
  updateProgressValue(progressValue3, 50);
  updateDataValue(circleProgressBar1, 0.50);
  updateDataValue(circleProgressBar2, 0.25);
  updateDataValue(circleProgressBar3, 0.50);
});

// Agregar un controlador de eventos de clic al tercer elemento de imagen de origen
sourceImage3.addEventListener("click", function() {
  var sourceImageUrl = sourceImage3.src;
  destinationImage.src = sourceImageUrl;
  updateProgressValue(progressValue1, 80);
  updateProgressValue(progressValue2, 90);
  updateProgressValue(progressValue3, 45);
  updateDataValue(circleProgressBar1, 0.80);
  updateDataValue(circleProgressBar2, 0.90);
  updateDataValue(circleProgressBar3, 0.45);
});

// Agregar un controlador de eventos de clic al cuarto elemento de imagen de origen
sourceImage4.addEventListener("click", function() {
  var sourceImageUrl = sourceImage4.src;
  destinationImage.src = sourceImageUrl;
  updateProgressValue(progressValue1, 50);
  updateProgressValue(progressValue2, 20);
  updateProgressValue(progressValue3, 75);
  updateDataValue(circleProgressBar1, 0.50);
  updateDataValue(circleProgressBar2, 0.20);
  updateDataValue(circleProgressBar3, 0.75);
});

function updateProgressValue(element, newValue) {
  // Crear una animación de desplazamiento suave utilizando transform: translateY()
  element.style.transition = "transform 0.3s ease-in-out";
  element.style.transform = "translateY(20px)";

  // Esperar un breve tiempo antes de actualizar el valor
  setTimeout(function() {
    // Actualizar el valor de progreso
    element.textContent = newValue;

    // Reiniciar la transformación para mostrar el nuevo valor
    element.style.transition = "none";
    element.style.transform = "none";

  }, 300); // Esperar 300ms (0.3 segundos) antes de actualizar el valor
}

function updateDataValue(element, newValue) {
  // Actualizar el atributo data-value con el nuevo valor
  element.setAttribute("data-value", newValue);
}











DateTimePicker.prototype._int = function _int() {
  var targetInput = this._element.data('target-input');
  if (this._element.is('input')) {
      this.input = this._element;
  } else if (targetInput !== undefined) {
      if (targetInput === 'nearest') {
          this.input = this._element.find('input');
      } else {
          this.input = $(targetInput);
      }
  }

  this._dates = [];
  this._dates[0] = this.getMoment();
  this._viewDate = this.getMoment().clone();

  $.extend(true, this._options, this._dataToOptions());

  this.options(this._options);

  this._initFormatting();

  if (this.input !== undefined && this.input.is('input') && this.input.val().trim().length !== 0) {
      this._setValue(this._parseInputDate(this.input.val().trim()), 0);
  } else if (this._options.defaultDate && this.input !== undefined && this.input.attr('placeholder') === undefined) {
      this._setValue(this._options.defaultDate, 0);
  }
  if (this._options.inline) {
      this.show();
  }
};