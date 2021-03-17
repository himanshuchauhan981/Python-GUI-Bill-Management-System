import { Component, OnInit } from '@angular/core'
import { FormControl, FormGroup, Validators } from '@angular/forms'

import { UserService } from '../service/user.service'

@Component({
	selector: 'login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

	constructor(private userService: UserService) { }

	emailForm = new FormGroup({
		email: new FormControl('', [Validators.required, Validators.email]),
		password: new FormControl('', Validators.required)
	})

	mobileNumberForm = new FormGroup({
		mobileNumber: new FormControl('', [Validators.required])
	})

	get emailFormControls() { return this.emailForm.controls }

	get mobileNoFormControls() { return this.mobileNumberForm.controls }

	ngOnInit() { }

	loginUser(loginForm) {
		this.userService.loginUser(loginForm.value)
			.subscribe((res: Response) => {
				console.log(res)
			})
	}

}
