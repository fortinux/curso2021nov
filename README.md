# cursoPython2021nov

- instalar git en windows:     
-  Descargarlo de https://git-scm.com/downloads    

## Inicializar repositorio utilizando git
- Comandos en la terminal    
    
- iniciar git
`git init`   
     
- agregar el repositorio creado anteriormente en el cvs    
- Dos opciones: Repositorio red local y repositorio en Github.com    
`git remote add origin http://www/usuario/CursoPython2021nov.git`    
`git remote add origin https://github.com/fortinux/curso2021nov.git`

`git fetch origin master`    
`git fetch origin main`    
    
- obtener los ficheros del repositorio apenas creados    
`git pull origin master`     
`git status`        
    
- crear fichero .gitignore con los ficheros que no se quieren subir al repositorio    
`vim .gitignore`     
    
- agregar los ficheros al commit    
`git add .`    
`git commit -m "clase 1"`    
  
- Para github.com es necesario configurar el usuario:

`git config --global user.email "usuario@usuario.com"`   
`git config --global user.name "usuario"`    

- Subir los ficheros al repositorio    
`git push origin master`    
