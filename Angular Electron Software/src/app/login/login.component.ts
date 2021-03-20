import { AfterViewInit, Component, OnInit } from '@angular/core'
import { FormControl, FormGroup, Validators } from '@angular/forms'
import * as firebase from 'firebase'

import { UserService } from '../service/user.service'
import { AngularFireAuth } from '@angular/fire/auth'
import { credentials } from '../../environments/firebase_credentials'

@Component({
	selector: 'login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, AfterViewInit {

	constructor(private userService: UserService, private auth: AngularFireAuth) { }

	showPassword: boolean = false;

	hideEmailLogin: boolean = false;

	windowRef: any;

	loginForm = new FormGroup({
		username: new FormControl('', Validators.required)
	})

	otpForm = new FormGroup({
		otp: new FormControl('', Validators.required)
	})

	passwordForm = new FormGroup({
		password: new FormControl('', Validators.required)
	})

	get passwordFormControls() { return this.passwordForm.controls }

	get loginFormControls() { return this.loginForm.controls }

	get otpFormControls() { return this.otpForm.controls }

	ngOnInit() {
		this.windowRef = this.userService.windowRef;
		firebase.default.initializeApp(credentials)
	}

	ngAfterViewInit() {
		this.windowRef.recaptchaVerifier = new firebase.default.auth.RecaptchaVerifier('recaptcha-container')
		this.windowRef.recaptchaVerifier.render()
	}



	showPasswordDialog() {
		let credentials: string = this.loginFormControls['username'].value;

		if (credentials.includes('@')) {
			this.showPassword = true;

		}
		else if (/^\d+$/.test(credentials)) {
			this.showPassword = true;
			this.hideEmailLogin = true;
		}
		else {
			this.loginFormControls['username'].setErrors({ 'incorrect': true })
		}
	}

	loginUser(form: FormGroup) {
		let email = this.loginFormControls['username'].value;
		let password = this.passwordFormControls['password'].value;

		if (form.valid) {
			console.log(form.controls)
			// this.userService.loginUser({ email, password }).subscribe(res => { })
		}

	}

}
