import { ComponentFixture, TestBed } from "@angular/core/testing";

import { UserProfileFormCard } from "./user-profile-form-card";

describe("UserProfileFormCard", () => {
	let component: UserProfileFormCard;
	let fixture: ComponentFixture<UserProfileFormCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [UserProfileFormCard],
		}).compileComponents();

		fixture = TestBed.createComponent(UserProfileFormCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
