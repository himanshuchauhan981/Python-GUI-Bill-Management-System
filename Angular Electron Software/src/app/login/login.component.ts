import { Component, OnInit } from '@angular/core'
import { FormControl, FormGroup } from '@angular/forms'

import { ApiService } from '../service/api.service'

@Component({
	selector: 'login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

	constructor(private apiService: ApiService) { }

	loginForm = new FormGroup({
		email: new FormControl(''),
		password: new FormControl('')
	})

	get email(){ return this.loginForm.get('email') }

	get password(){ return this.loginForm.get('password') }

	ngOnInit() { }

	loginUser(loginForm){
		this.apiService.loginUser(loginForm.value)
		.subscribe((res: Response)=>{
			console.log(res)
		})
		// this.apiService.loginUser(loginForm.value)
		// 	.subscribe((res)=>{
		// 		console.log(res)
		// 	})
	}

}
