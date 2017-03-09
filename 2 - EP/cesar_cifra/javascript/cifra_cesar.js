alphaDefault = new Array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
alphaCrypted = new Array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');

var rotate = 0;
var cryptLevel = 1;

function reCrypt(comando, mensagem, rotate, cryptLevel) {

    if (comando == "encrypt") {
        for (var i = 0; i < cryptLevel; i++) {
            rotateAlpha(rotate);
            mensagem = encrypt(mensagem);
        }
    } else if (comando == "decrypt") {
        for (var i = 0; i < cryptLevel; i++) {
            rotateAlpha(rotate);
            mensagem = decrypt(mensagem);
        }
    }

    return mensagem;
}

function rotateAlpha(rotate) {
    var countPositivo = 26 - rotate;
    for (var i = 0 & countPositivo; i < rotate; i++ & countPositivo++) {
        alphaCrypted[countPositivo] = alphaDefault[i];
    }

    j = rotate;
    for (var i = 0 & j; j < 26; i++ & j++) {
        alphaCrypted[i] = alphaDefault[j];
        //console.log('i->', i, 'j->', j);
    }
}

function decrypt(mensagem) {

    msgEncrypting = "";
    mensagemFormated = (mensagem.toLowerCase());

    for (var i = 0; i < mensagemFormated.length; i++) {
        if ((alphaDefault.indexOf(mensagemFormated[i]) != -1)) {
            var j = alphaCrypted.indexOf(mensagemFormated[i]);
            msgEncrypting += alphaDefault[j];
        } else {
            msgEncrypting += mensagemFormated[i];
        }
    }
    return msgEncrypting;
}

function encrypt(mensagem) {
    msgEncrypting = [];
    mensagemFormated = (mensagem.toLowerCase());

    for (var i = 0; i < mensagemFormated.length; i++) {
        if ((alphaDefault.indexOf(mensagemFormated[i]) != -1)) {
            var j = alphaDefault.indexOf(mensagemFormated[i]);
            msgEncrypting += alphaCrypted[j];
        } else {
            msgEncrypting += mensagemFormated[i];
        }
    }
    return msgEncrypting;
}

function msgEncrypted(txtInput) {

    var msgCriptograda = reCrypt("encrypt", txtInput.value + '', rotate, cryptLevel);

    return msgCriptograda;
}

function msgDescrypted(txtInput) {

    var msgDescriptografada = reCrypt("decrypt", txtInput.value + '', rotate, cryptLevel);

    return msgDescriptografada;

}

function main() {


    var btnEncrypt = document.getElementById("btnEncrypt");
    var btnDecrypt = document.getElementById("btnDecrypt");

    var btnRotateAdd = document.getElementById("btnRotateAdd");
    var btnRotateDec = document.getElementById("btnRotateDec");
    var btnCryptLevelAdd = document.getElementById("btnCryptLevelAdd");
    var btnCryptLevelDec = document.getElementById("btnCryptLevelDec");

    var txtInput = document.getElementById("txtInput");
    var txtOutput = document.getElementById("txtOutput");

    var rotateValue = document.getElementById('rotateValue');

    rotateCryptLevel.setAttribute("data-text", cryptLevel + '');

    btnEncrypt.onclick = function() {

        rotateAlpha(rotate);

        var msgCriptografada = msgEncrypted(txtInput);
        txtOutput.value = msgCriptografada;
    };

    btnDecrypt.onclick = function() {

        var msgDescriptografada = msgDescrypted(txtInput);
        txtOutput.value = msgDescriptografada;
    };

    btnRotateAdd.onclick = function() {

        if (rotate >= 0 && rotate < 13) {
            rotate++;
            rotateValue.setAttribute('data-text', rotate + '');
        }

        var msgCriptografada = msgEncrypted(txtInput);
        txtOutput.value = msgCriptografada;
    };

    btnRotateDec.onclick = function() {

        if (rotate > 0 && rotate <= 13) {
            rotate--;
            rotateValue.setAttribute("data-text", rotate + '');
        }

        var msgCriptografada = msgEncrypted(txtInput);
        txtOutput.value = msgCriptografada;
    };

    btnCryptLevelAdd.onclick = function() {

        if (cryptLevel <= 0 && cryptLevel > 13) {
            cryptLevel++;
            rotateCryptLevel.setAttribute("data-text", cryptLevel + '');
        }
        var msgCriptograda = msgEncrypted(txtInput);
        txtOutput.value = msgCriptograda;

        var msgDescriptografada = msgDescrypted(txtInput);

    };

    btnCryptLevelDec.onclick = function() {

        if (cryptLevel > 0) {
            cryptLevel--;
            rotateCryptLevel.setAttribute("data-text", cryptLevel + '');
        }

        var msgCriptograda = msgEncrypted(txtInput);
        txtOutput.value = msgCriptograda;

    };
}