import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ServiceCreateDialog } from "./service-create-dialog";

describe("ServiceCreateDialog", () => {
	let component: ServiceCreateDialog;
	let fixture: ComponentFixture<ServiceCreateDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ServiceCreateDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ServiceCreateDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
