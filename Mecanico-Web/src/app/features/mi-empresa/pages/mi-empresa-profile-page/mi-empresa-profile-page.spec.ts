import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaProfilePage } from "./mi-empresa-profile-page";

describe("MiEmpresaProfilePage", () => {
	let component: MiEmpresaProfilePage;
	let fixture: ComponentFixture<MiEmpresaProfilePage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaProfilePage],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaProfilePage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
