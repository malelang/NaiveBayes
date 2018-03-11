<html>
   <head>
      <title>The Materialize Form Example</title>
      <meta name = "viewport" content = "width = device-width, initial-scale = 1">
      <link rel = "stylesheet"
         href = "https://fonts.googleapis.com/icon?family=Material+Icons">
      <link rel = "stylesheet"
         href = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/css/materialize.min.css">
      <script type = "text/javascript"
         src = "https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script src = "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js">
      </script>
   </head>
   <body class = "container">
        <nav>
          <div class="nav-wrapper">
            <a href="#" class="brand-logo center">Mineria de Datos</a>
          </div>
        </nav>
        <nav>
          <div class="nav-wrapper">
            <ul id="nav-mobile" class="left hide-on-med-and-down">
              <li><a href="index.php">Inicio</a></li>
              <li><a href="send.php">Guardar Registros</a></li>
              <li><a href="list.php">Listar Registros</a></li>
              <li><a href= "cross.php">Validacion cruzada</a><li>
            </ul>
          </div>
        </nav>
        <br>
        <hr>
        <br>
        <div class = "row">
           <form class = "col s12" action="savecross.php" method="POST">
              <div class = "row">

                 <div class = "input-field col s6">
                 <i class = "material-icons prefix">account_circle</i>
                    <input placeholder = "e.g.1,2"  id = "cruces" name = "cruces"
                       type = "number"  min ="1" max="5" required />
                    <label for = "name">Numero de pliegues</label>
                 </div>
              </div>


        <div class="row">

        <button class="btn waves-effect waves-light" type="submit" name="action">Aplicar
             <i class="material-icons right">cross</i>
        </button>
        </div>
        </form>
      </div>
    </body>
</html>
