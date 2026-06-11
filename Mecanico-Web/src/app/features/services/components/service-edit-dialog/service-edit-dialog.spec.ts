import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ServiceEditDialog } from "./service-edit-dialog";

describe("ServiceEditDialog", () => {
	let component: ServiceEditDialog;
	let fixture: ComponentFixture<ServiceEditDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ServiceEditDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ServiceEditDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
