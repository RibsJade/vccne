server {
        listen 80;
        listen [::]:80;
	
	root /var/www;
	
	
        server_name vxne.com, www.vxne.com;

        location /Back {
		proxy_set_header Host $http_host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header Upgrade $http_upgrade;
                #proxy_set_header Connection $connection_upgrade;
                proxy_redirect off;
                proxy_buffering off;
		proxy_pass http://localhost:5000;
	}

	location /vxne.com/Front/ {
		alias /var/www/vxne.com/Front/;
		index index.php; 
		try_files $uri $uri/ =404;
        }

	
	location ~ \.php$ {
        #try_files $uri;
        include fastcgi_params;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/run/php/php7.4-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }

}
