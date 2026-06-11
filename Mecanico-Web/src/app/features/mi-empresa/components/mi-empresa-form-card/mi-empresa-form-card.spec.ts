import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaFormCard } from "./mi-empresa-form-card";

describe("MiEmpresaFormCard", () => {
	let component: MiEmpresaFormCard;
	let fixture: ComponentFixture<MiEmpresaFormCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaFormCard],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaFormCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
