import { ComponentFixture, TestBed } from "@angular/core/testing";

import { UserProfileRolesCard } from "./user-profile-roles-card";

describe("UserProfileRolesCard", () => {
	let component: UserProfileRolesCard;
	let fixture: ComponentFixture<UserProfileRolesCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [UserProfileRolesCard],
		}).compileComponents();

		fixture = TestBed.createComponent(UserProfileRolesCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
