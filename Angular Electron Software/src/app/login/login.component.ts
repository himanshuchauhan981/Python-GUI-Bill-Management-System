import { Component, OnInit } from '@angular/core'
import { FormControl, FormGroup, Validators } from '@angular/forms'

import { ApiService } from '../service/api.service'

@Component({
	selector: 'login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

	constructor(private apiService: ApiService) { }

	loginForm = new FormGroup({
		email: new FormControl('', [Validators.required, Validators.email]),
		password: new FormControl('', Validators.required)
	})

	get loginFormControls() { return this.loginForm.controls }

	ngOnInit() { }

	loginUser(loginForm) {
		this.apiService.loginUser(loginForm.value)
			.subscribe((res: Response) => {
				console.log(res)
			})
	}

}
