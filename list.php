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

    <!-- Tabla Responsive para mostrar los registros -->
    <table class="bordered">
        <thead>
          <tr>
              <th>Edad</th>
              <th>Nivel de sodio</th>
              <th>Nivel de potasio</th>
              <th>Genero</th>
              <th>Presion Sanguinea</th>
              <th>Colesterol</th>
              <th>Drug Recommended</th>

          </tr>
        </thead>

        <tbody>
            <?php


            $file_handle = fopen("registrosProcesados.txt", "rb");

            while (!feof($file_handle) ) {
                $line_of_text = fgets($file_handle);
                $parts = explode('--', $line_of_text);
                echo "<tr><td >$parts[0]</td><td>$parts[1]</td><td>$parts[2]</td><td>$parts[3]</td><td>$parts[4]</td><td>$parts[5]
                </td><td><b>$parts[6]</b></td></tr>";
            }
            fclose($file_handle);

            ?>

        </tbody>
      </table>

   </body>
</html>
